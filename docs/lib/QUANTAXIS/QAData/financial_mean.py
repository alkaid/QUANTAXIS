# coding:utf-8

financial_dict = {
    # 1.每股指标
    '基本每股收益': 'EPS',
    '扣除非经常性损益每股收益': 'deductEPS',
    '每股未分配利润': 'undistributedProfitPerShare',
    '每股净资产': 'netAssetsPerShare',
    '每股资本公积金': 'capitalReservePerShare',
    '净资产收益率': 'ROE',
    '每股经营现金流量': 'operatingCashFlowPerShare',
    # 2. 资产负债表 BALANCE SHEET
    # 2.1 资产
    # 2.1.1 流动资产
    '货币资金': 'moneyFunds',
    '交易性金融资产': 'tradingFinancialAssets',
    '应收票据': 'billsReceivables',
    '应收账款': 'accountsReceivables',
    '预付款项': 'prepayments',
    '其他应收款': 'otherReceivables',
    '应收关联公司款': 'interCompanyReceivables',
    '应收利息': 'interestReceivables',
    '应收股利': 'dividendsReceivables',
    '存货': 'inventory',
    '其中：消耗性生物资产': 'expendableBiologicalAssets',
    '一年内到期的非流动资产': 'noncurrentAssetsDueWithinOneYear',
    '其他流动资产': 'otherLiquidAssets',
    '流动资产合计': 'totalLiquidAssets',
    # 2.1.2 非流动资产
    '可供出售金融资产': 'availableForSaleSecurities',
    '持有至到期投资': 'heldToMaturityInvestments',
    '长期应收款': 'longTermReceivables',
    '长期股权投资': 'longTermEquityInvestment',
    '投资性房地产': 'investmentRealEstate',
    '固定资产': 'fixedAssets',
    '在建工程': 'constructionInProgress',
    '工程物资': 'engineerMaterial',
    '固定资产清理': 'fixedAssetsCleanUp',
    '生产性生物资产': 'productiveBiologicalAssets',
    '油气资产': 'oilAndGasAssets',
    '无形资产': 'intangibleAssets',
    '开发支出': 'developmentExpenditure',
    '商誉': 'goodwill',
    '长期待摊费用': 'longTermDeferredExpenses',
    '递延所得税资产': 'deferredIncomeTaxAssets',
    '其他非流动资产': 'otherNonCurrentAssets',
    '非流动资产合计': 'totalNonCurrentAssets',
    '资产总计': 'totalAssets',
    # 2.2 负债
    # 2.2.1 流动负债
    '短期借款': 'shortTermLoan',
    '交易性金融负债': 'tradingFinancialLiabilities',
    '应付票据': 'billsPayable',
    '应付账款': 'accountsPayable',
    '预收款项': 'advancedReceivable',
    '应付职工薪酬': 'employeesPayable',
    '应交税费': 'taxPayable',
    '应付利息': 'interestPayable',
    '应付股利': 'dividendPayable',
    '其他应付款': 'otherPayable',
    '应付关联公司款': 'interCompanyPayable',
    '一年内到期的非流动负债': 'noncurrentLiabilitiesDueWithinOneYear',
    '其他流动负债': 'otherCurrentLiabilities',
    '流动负债合计': 'totalCurrentLiabilities',
    # 2.2.2 非流动负债
    '长期借款': 'longTermLoans',
    '应付债券': 'bondsPayable',
    '长期应付款': 'longTermPayable',
    '专项应付款': 'specialPayable',
    '预计负债': 'estimatedLiabilities',
    '递延所得税负债': 'defferredIncomeTaxLiabilities',
    '其他非流动负债': 'otherNonCurrentLiabilities',
    '非流动负债合计': 'totalNonCurrentLiabilities',
    '负债合计': 'totalLiabilities',
    # 2.3 所有者权益
    '实收资本（或股本）': 'totalShare',
    '资本公积': 'capitalReserve',
    '盈余公积': 'surplusReserve',
    '减：库存股': 'treasuryStock',
    '未分配利润': 'undistributedProfits',
    '少数股东权益': 'minorityEquity',
    '外币报表折算价差': 'foreignCurrencyReportTranslationSpread',
    '非正常经营项目收益调整': 'abnormalBusinessProjectEarningsAdjustment',
    '所有者权益（或股东权益）合计': 'totalOwnersEquity',
    '负债和所有者（或股东权益）合计': 'totalLiabilitiesAndOwnersEquity',
    # 3. 利润表
    '其中：营业收入': 'operatingRevenue',
    '其中：营业成本': 'operatingCosts',
    '营业税金及附加': 'taxAndSurcharges',
    '销售费用': 'salesCosts',
    '管理费用': 'managementCosts',
    '堪探费用': 'explorationCosts',
    '财务费用': 'financialCosts',
    '资产减值损失': 'assestsDevaluation',
    '加：公允价值变动净收益': 'profitAndLossFromFairValueChanges',
    '投资收益': 'investmentIncome',
    '其中：对联营企业和合营企业的投资收益': 'investmentIncomeFromAffiliatedBusinessAndCooperativeEnterprise',
    '影响营业利润的其他科目': 'otherSubjectsAffectingOperatingProfit',
    '三、营业利润': 'operatingProfit',
    '加：补贴收入': 'subsidyIncome',
    '营业外收入': 'nonOperatingIncome',
    '减：营业外支出': 'nonOperatingExpenses',
    '其中：非流动资产处置净损失': 'netLossFromDisposalOfNonCurrentAssets',
    '加：影响利润总额的其他科目': 'otherSubjectsAffectTotalProfit',
    '四、利润总额': 'totalProfit',
    '减：所得税': 'incomeTax',
    '加：影响净利润的其他科目': 'otherSubjectsAffectNetProfit',
    '五、净利润': 'netProfit',
    '归属于母公司所有者的净利润': 'netProfitsBelongToParentCompanyOwner',
    '少数股东损益': 'minorityProfitAndLoss',

    # 4. 现金流量表
    # 4.1 经营活动 Operating
    '销售商品、提供劳务收到的现金': 'cashFromGoodsSalesorOrRenderingOfServices',
    '收到的税费返还': 'refundOfTaxAndFeeReceived',
    '收到其他与经营活动有关的现金': 'otherCashRelatedBusinessActivitiesReceived',
    '经营活动现金流入小计': 'cashInflowsFromOperatingActivities',
    '购买商品、接受劳务支付的现金': 'buyingGoodsReceivingCashPaidForLabor',
    '支付给职工以及为职工支付的现金': 'paymentToEmployeesAndCashPaidForEmployees',
    '支付的各项税费': 'paymentsOfVariousTaxes',
    '支付其他与经营活动有关的现金': 'paymentOfOtherCashRelatedToBusinessActivities',
    '经营活动现金流出小计': 'cashOutflowsFromOperatingActivities',
    '经营活动产生的现金流量净额': 'netCashFlowsFromOperatingActivities',
    # 4.2 投资活动 Investment
    '收回投资收到的现金': 'cashReceivedFromInvestmentReceived',
    '取得投资收益收到的现金': 'cashReceivedFromInvestmentIncome',
    '处置固定资产、无形资产和其他长期资产收回的现金净额': 'disposalOfNetCashForRecoveryOfFixedAssetsIntangibleAssetsAndOtherLongTermAssets',
    '处置子公司及其他营业单位收到的现金净额': 'disposalOfNetCashReceivedFromSubsidiariesAndOtherBusinessUnits',
    '收到其他与投资活动有关的现金': 'otherCashReceivedRelatingToInvestingActivities',
    '投资活动现金流入小计': 'cashinFlowsFromInvestmentActivities',
    '购建固定资产、无形资产和其他长期资产支付的现金': 'cashForThePurchaseConstructionPaymentOfFixedAssetsIntangibleAssetsAndOtherLongTermAssets',
    '投资支付的现金': 'cashInvestment',
    '取得子公司及其他营业单位支付的现金净额': 'acquisitionOfNetCashPaidBySubsidiariesAndOtherBusinessUnits',
    '支付其他与投资活动有关的现金': 'otherCashPaidRelatingToInvestingActivities',
    '投资活动现金流出小计': 'cashOutflowsFromInvestmentActivities',
    '投资活动产生的现金流量净额': 'netCashFlowsFromInvestingActivities',
    # 4.3 筹资活动 Financing
    '吸收投资收到的现金': 'cashReceivedFromInvestors',
    '取得借款收到的现金': 'cashFromBorrowings',
    '收到其他与筹资活动有关的现金': 'otherCashReceivedRelatingToFinancingActivities',
    '筹资活动现金流入小计': 'cashInflowsFromFinancingActivities',
    '偿还债务支付的现金': 'cashPaymentsOfAmountBorrowed',
    '分配股利、利润或偿付利息支付的现金': 'cashPaymentsForDistrbutionOfDividendsOrProfits',
    '支付其他与筹资活动有关的现金': 'otherCashPaymentRelatingToFinancingActivities',
    '筹资活动现金流出小计': 'cashOutflowsFromFinancingActivities',
    '筹资活动产生的现金流量净额': 'netCashFlowsFromFinancingActivities',
    # 4.4 汇率变动
    '四、汇率变动对现金的影响': 'effectOfForeignExchangRateChangesOnCash',
    '四(2)、其他原因对现金的影响': 'effectOfOtherReasonOnCash',
    # 4.5 现金及现金等价物净增加
    '五、现金及现金等价物净增加额': 'netIncreaseInCashAndCashEquivalents',
    '期初现金及现金等价物余额': 'initialCashAndCashEquivalentsBalance',
    # 4.6 期末现金及现金等价物余额
    '期末现金及现金等价物余额': 'theFinalCashAndCashEquivalentsBalance',
    # 4.x 补充项目 Supplementary Schedule：
    # 现金流量附表项目    Indirect Method
    # 4.x.1 将净利润调节为经营活动现金流量 Convert net profit to cash flow from operating activities
    '净利润': 'netProfit',
    '加：资产减值准备': 'provisionForAssetsLosses',
    '固定资产折旧、油气资产折耗、生产性生物资产折旧': 'depreciationForFixedAssets',
    '无形资产摊销': 'amortizationOfIntangibleAssets',
    '长期待摊费用摊销': 'amortizationOfLong-termDeferredExpenses',
    '处置固定资产、无形资产和其他长期资产的损失': 'lossOfDisposingFixedAssetsIntangibleAssetsAndOtherLong-termAssets',
    '固定资产报废损失': 'scrapLossOfFixedAssets',
    '公允价值变动损失': 'lossFromFairValueChange',
    '财务费用': 'financialExpenses',
    '投资损失': 'investmentLosses',
    '递延所得税资产减少': 'decreaseOfDeferredTaxAssets',
    '递延所得税负债增加': 'increaseOfDeferredTaxLiabilities',
    '存货的减少': 'decreaseOfInventory',
    '经营性应收项目的减少': 'decreaseOfOperationReceivables',
    '经营性应付项目的增加': 'increaseOfOperationPayables',
    '其他': 'others',
    '经营活动产生的现金流量净额2': 'netCashFromOperatingActivities2',
    # 4.x.2 不涉及现金收支的投资和筹资活动 Investing and financing activities not involved in cash
    '债务转为资本': 'debtConvertedToCSapital',
    '一年内到期的可转换公司债券': 'convertibleBondMaturityWithinOneYear',
    '融资租入固定资产': 'leaseholdImprovements',
    # 4.x.3 现金及现金等价物净增加情况 Net increase of cash and cash equivalents
    '现金的期末余额': 'cashEndingBal',
    '减：现金的期初余额': 'cashBeginingBal',
    '加：现金等价物的期末余额': 'cashEquivalentsEndingBal',
    '减：现金等价物的期初余额': 'cashEquivalentsBeginningBal',
    '现金及现金等价物净增加额': 'netIncreaseOfCashAndCashEquivalents',
    # 5. 偿债能力分析
    '流动比率': 'liquidityRatio',  # 流动资产/流动负债
    '速动比率': 'acidTestRatio',  # (流动资产-存货）/流动负债
    '现金比率(%)': 'cashRatio',  # (货币资金+有价证券)÷流动负债
    '利息保障倍数': 'interestCoverageRatio',  # (利润总额+财务费用（仅指利息费用部份）)/利息费用
    '非流动负债比率(%)': 'noncurrentLiabilitiesRatio',
    '流动负债比率(%)': 'currentLiabilitiesRatio',
    '现金到期债务比率(%)': 'cashDebtRatio',  # 企业经营现金净流入/(本期到期长期负债+本期应付票据)
    '有形资产净值债务率(%)': 'debtToTangibleAssetsRatio',
    '权益乘数(%)': 'equityMultiplier',  # 资产总额/股东权益总额
    '股东的权益/负债合计(%)': 'equityDebtRatio',  # 权益负债率
    '有形资产/负债合计(%)': 'tangibleAssetDebtRatio ',  # 有形资产负债率
    '经营活动产生的现金流量净额/负债合计(%)': 'netCashFlowsFromOperatingActivitiesDebtRatio',
    'EBITDA/负债合计(%)': 'EBITDA/Liabilities',
    # 6. 经营效率分析
    # 销售收入÷平均应收账款=销售收入\(0.5 x(应收账款期初+期末))
    '应收帐款周转率': 'turnoverRatioOfReceivable;',
    '存货周转率': 'turnoverRatioOfInventory',
    # (存货周转天数+应收帐款周转天数-应付帐款周转天数+预付帐款周转天数-预收帐款周转天数)/365
    '运营资金周转率': 'turnoverRatioOfOperatingAssets',
    '总资产周转率': 'turnoverRatioOfTotalAssets',
    '固定资产周转率': 'turnoverRatioOfFixedAssets',  # 企业销售收入与固定资产净值的比率
    '应收帐款周转天数': 'daysSalesOutstanding',  # 企业从取得应收账款的权利到收回款项、转换为现金所需要的时间
    '存货周转天数': 'daysSalesOfInventory',  # 企业从取得存货开始，至消耗、销售为止所经历的天数
    '流动资产周转率': 'turnoverRatioOfCurrentAssets',  # 流动资产周转率(次)=主营业务收入/平均流动资产总额
    '流动资产周转天数': 'daysSalesofCurrentAssets',
    '总资产周转天数': 'daysSalesofTotalAssets',
    '股东权益周转率': 'equityTurnover',  # 销售收入/平均股东权益
    '营业收入增长率(%)': 'operatingIncomeGrowth',
    # 7. 发展能力分析
    '净利润增长率(%)': 'netProfitGrowthRate',  # NPGR  利润总额－所得税
    '净资产增长率(%)': 'netAssetsGrowthRate',
    '固定资产增长率(%)': 'fixedAssetsGrowthRate',
    '总资产增长率(%)': 'totalAssetsGrowthRate',
    '投资收益增长率(%)': 'investmentIncomeGrowthRate',
    '营业利润增长率(%)': 'operatingProfitGrowthRate',
    '暂无': 'None1',
    '暂无': 'None2',
    '暂无': 'None3',
    # 8. 获利能力分析
    '成本费用利润率(%)': 'rateOfReturnOnCost',
    '营业利润率': 'rateOfReturnOnOperatingProfit',
    '营业税金率': 'rateOfReturnOnBusinessTax',
    '营业成本率': 'rateOfReturnOnOperatingCost',
    '净资产收益率': 'rateOfReturnOnCommonStockholdersEquity',
    '投资收益率': 'rateOfReturnOnInvestmentIncome',
    '销售净利率(%)': 'rateOfReturnOnNetSalesProfit',
    '总资产报酬率': 'rateOfReturnOnTotalAssets',
    '净利润率': 'netProfitMargin',
    '销售毛利率(%)': 'rateOfReturnOnGrossProfitFromSales',
    '三费比重': 'threeFeeProportion',
    '管理费用率': 'ratioOfChargingExpense',
    '财务费用率': 'ratioOfFinancialExpense',
    '扣除非经常性损益后的净利润': 'netProfitAfterExtraordinaryGainsAndLosses',
    '息税前利润(EBIT)': 'EBIT',
    '息税折旧摊销前利润(EBITDA)': 'EBITDA',
    'EBITDA/营业总收入(%)': 'EBITDA/GrossRevenueRate',
    # 9. 资本结构分析
    '资产负债率(%)': 'assetsLiabilitiesRatio',
    '流动资产比率': 'liquidityRatio',
    '货币资金比率': 'monetaryFundRatio',
    '存货比率': 'inventoryRatio',
    '固定资产比率': 'fixedAssetsRatio',
    '负债结构比': 'liabilitiesStructureRatio',
    '归属于母公司股东权益/全部投入资本(%)': 'shareholdersOwnershipOfAParentCompany/TotalCapital',
    '股东的权益/带息债务(%)': 'shareholdersInterest/InterestRateDebtRatio',
    '有形资产/净债务(%)': 'tangibleAssets/NetDebtRatio',
    # 10. 现金流量分析
    '每股经营性现金流(元)': 'operatingCashFlowPerShare',
    '营业收入现金含量(%)': 'cashOfOperatingIncome',
    '经营活动产生的现金流量净额/经营活动净收益(%)': 'netOperatingCashFlow/netOperationProfit',
    '销售商品提供劳务收到的现金/营业收入(%)': 'cashFromGoodsSales/OperatingRevenue',
    '经营活动产生的现金流量净额/营业收入': 'netOperatingCashFlow/OperatingRevenue',
    '资本支出/折旧和摊销': 'capitalExpenditure/DepreciationAndAmortization',
    '每股现金流量净额(元)': 'netCashFlowPerShare',
    '经营净现金比率（短期债务）': 'operatingCashFlow/ShortTermDebtRatio',
    '经营净现金比率（全部债务）': 'operatingCashFlow/LongTermDebtRatio',
    '经营活动现金净流量与净利润比率': 'cashFlowRateAndNetProfitRatioOfOperatingActivities',
    '全部资产现金回收率': 'cashRecoveryForAllAssets',
    # 11. 单季度财务指标
    '营业收入': 'operatingRevenue',
    '营业利润': 'operatingProfit',
    '归属于母公司所有者的净利润': 'netProfitBelongingToTheOwnerOfTheParentCompany',
    '扣除非经常性损益后的净利润': 'netProfitAfterExtraordinaryGainsAndLosses',
    '经营活动产生的现金流量净额': 'netCashFlowsFromOperatingActivities',
    '投资活动产生的现金流量净额': 'netCashFlowsFromInvestingActivities',
    '筹资活动产生的现金流量净额': 'netCashFlowsFromFinancingActivities',
    '现金及现金等价物净增加额': 'netIncreaseInCashAndCashEquivalents',
    # 12.股本股东
    '总股本': 'totalCapital',
    '已上市流通A股': 'listedAShares',
    '已上市流通B股': 'listedBShares',
    '已上市流通H股': 'listedHShares',
    '股东人数(户)': 'numberOfShareholders',
    '第一大股东的持股数量': 'theNumberOfFirstMajorityShareholder',
    '十大流通股东持股数量合计(股)': 'totalNumberOfTopTenCirculationShareholders',
    '十大股东持股数量合计(股)': 'totalNumberOfTopTenMajorShareholders',
    # 13.机构持股
    '机构总量（家）': 'institutionNumber',
    '机构持股总量(股)': 'institutionShareholding',
    'QFII机构数': 'QFIIInstitutionNumber',
    'QFII持股量': 'QFIIShareholding',
    '券商机构数': 'brokerNumber',
    '券商持股量': 'brokerShareholding',
    '保险机构数': 'securityNumber',
    '保险持股量': 'securityShareholding',
    '基金机构数': 'fundsNumber',
    '基金持股量': 'fundsShareholding',
    '社保机构数': 'socialSecurityNumber',
    '社保持股量': 'socialSecurityShareholding',
    '私募机构数': 'privateEquityNumber',
    '私募持股量': 'privateEquityShareholding',
    '财务公司机构数': 'financialCompanyNumber',
    '财务公司持股量': 'financialCompanyShareholding',
    '年金机构数': 'pensionInsuranceAgencyNumber',
    '年金持股量': 'pensionInsuranceAgencyShareholfing',
    # 14.新增指标
    # [注：季度报告中，若股东同时持有非流通A股性质的股份(如同时持有流通A股和流通B股），取的是包含同时持有非流通A股性质的流通股数]
    '十大流通股东中持有A股合计(股)': 'totalNumberOfTopTenCirculationShareholders',
    '第一大流通股东持股量(股)': 'firstLargeCirculationShareholdersNumber',
    # [注：1.自由流通股=已流通A股-十大流通股东5%以上的A股；2.季度报告中，若股东同时持有非流通A股性质的股份(如同时持有流通A股和流通H股），5%以上的持股取的是不包含同时持有非流通A股性质的流通股数，结果可能偏大； 3.指标按报告期展示，新股在上市日的下个报告期才有数据]
    '自由流通股(股)': 'freeCirculationStock',
    '受限流通A股(股)': 'limitedCirculationAShares',
    '一般风险准备(金融类)': 'generalRiskPreparation',
    '其他综合收益(利润表)': 'otherComprehensiveIncome',
    '综合收益总额(利润表)': 'totalComprehensiveIncome',
    '归属于母公司股东权益(资产负债表)': 'shareholdersOwnershipOfAParentCompany ',
    '银行机构数(家)(机构持股)': 'bankInstutionNumber',
    '银行持股量(股)(机构持股)': 'bankInstutionShareholding',
    '一般法人机构数(家)(机构持股)': 'corporationNumber',
    '一般法人持股量(股)(机构持股)': 'corporationShareholding',
    '近一年净利润(元)': 'netProfitLastYear'
}
